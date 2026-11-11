"""Validate repository images, recorded hashes, JSON and local documentation links.
Run from any directory: python analise/validar_integridade.py
Requires Pillow and NumPy. Does not modify assets.
"""
from pathlib import Path
import hashlib, json, re, argparse, subprocess
from urllib.parse import unquote, urlsplit
from PIL import Image
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--output', default='analise/integridade.json')
args = parser.parse_args()
source_commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
errors, images, links = [], [], 0
for p in sorted(ROOT.rglob('*')):
    if '.git' in p.parts or not p.is_file():
        continue
    rel = p.relative_to(ROOT).as_posix()
    if p.suffix.lower() in ('.png', '.gif'):
        try:
            with Image.open(p) as im:
                im.verify()
            with Image.open(p) as im:
                count = getattr(im, 'n_frames', 1)
                durations, bounds = [], []
                for i in range(count):
                    im.seek(i)
                    im.load()
                    if count > 1:
                        durations.append(im.info.get('duration'))
                    if p.suffix == '.png':
                        cols, rows = (4, 2) if 'idle' in p.name.lower() else (1, 1)
                        for y in range(rows):
                            for x in range(cols):
                                box = (round(x*im.width/cols), round(y*im.height/rows), round((x+1)*im.width/cols), round((y+1)*im.height/rows))
                                a = np.asarray(im.convert('RGB').crop(box))
                                mask = ~((a[:,:,0] > 220) & (a[:,:,1] < 70) & (a[:,:,2] > 220))
                                yy, xx = np.where(mask)
                                if len(xx):
                                    margins = [int(xx.min()), int(yy.min()), int(a.shape[1]-1-xx.max()), int(a.shape[0]-1-yy.max())]
                                    bounds.append(margins)
                                    if min(margins) == 0:
                                        errors.append(f'{rel}: foreground touches cell boundary {x},{y}')
                                else:
                                    errors.append(f'{rel}: empty cell {x},{y}')
                images.append(dict(path=rel, size=list(im.size), mode=im.mode, frames=count, frame_ms=durations, loop=im.info.get('loop'), bytes=p.stat().st_size, sha256=hashlib.sha256(p.read_bytes()).hexdigest(), approximate_cell_margins_ltrb=bounds))
                if p.suffix == '.gif' and (count != 8 or durations != [120]*8):
                    errors.append(f'{rel}: unexpected preview frames/timing')
        except Exception as exc:
            errors.append(f'{rel}: {exc}')
    if p.suffix == '.json' and not rel.startswith('analise/integridade'):
        try:
            data = json.loads(p.read_text())
            def check(obj, candidate=None):
                if isinstance(obj, dict):
                    target = obj.get('path') or obj.get('file') or obj.get('image') or candidate
                    if target:
                        q = ROOT / target
                        if not q.exists():
                            q = p.parent / target
                        if not q.exists():
                            errors.append(f'{rel}: missing {target}')
                        elif q.is_file():
                            if 'sha256' in obj and hashlib.sha256(q.read_bytes()).hexdigest() != obj['sha256']:
                                errors.append(f'{rel}: hash mismatch {target}')
                            if 'bytes' in obj and q.stat().st_size != obj['bytes']:
                                errors.append(f'{rel}: byte count mismatch {target}')
                            if 'size' in obj and q.suffix in ('.png','.gif'):
                                with Image.open(q) as im:
                                    if list(im.size) != obj['size']:
                                        errors.append(f'{rel}: dimension mismatch {target}')
                    for key, value in obj.items():
                        child = None
                        if key == 'files' and isinstance(value, dict):
                            for ext, info in value.items():
                                check(info, p.with_suffix('.'+ext).relative_to(ROOT).as_posix())
                            continue
                        if key == 'sources' and isinstance(value, dict):
                            for name, info in value.items():
                                check(info, 'referencias/'+name)
                            continue
                        if key in ('sheet','preview'):
                            child = p.with_suffix('.png' if key == 'sheet' else '.gif').relative_to(ROOT).as_posix()
                        check(value, child)
                    for field in ('prompt','occlusion_contract'):
                        if isinstance(obj.get(field),str) and not (ROOT/obj[field]).exists():
                            errors.append(f'{rel}: missing {obj[field]}')
                    for ref in obj.get('references',[]):
                        if not (ROOT/ref).exists(): errors.append(f'{rel}: missing {ref}')
                elif isinstance(obj, list):
                    for item in obj: check(item)
            default = p.with_suffix('.png')
            check(data, default.relative_to(ROOT).as_posix() if default.exists() else None)
        except Exception as exc:
            errors.append(f'{rel}: {exc}')
    if p.suffix == '.md' or p.name == 'state.ai':
        s = p.read_text()
        targets = re.findall(r'\]\(([^)]+)\)', s) + re.findall(r'(?:src|href)="([^"]+)"', s)
        for raw in targets:
            raw = raw.strip('<>')
            if raw.startswith(('#','http:','https:','mailto:')):
                continue
            target = unquote(urlsplit(raw).path)
            if target:
                links += 1
                if not (p.parent / target).exists():
                    errors.append(f'{rel}: broken local link {raw}')
report = {'date':'2026-11-11','source_commit':source_commit,'image_count':len(images),'gif_frame_count':sum(x['frames'] for x in images if x['path'].endswith('.gif')),'local_links_checked':links,'errors':errors,'images':images,'limits':['Foreground boundary check is approximate; not semantic certification.','No engine, transparency, pivot or atlas validation.','No external URL availability checks.']}
(ROOT/args.output).write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='images'},ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
