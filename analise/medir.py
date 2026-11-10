"""Mede fontes sem alterá-las. Execute: python analise/medir.py."""
from pathlib import Path
from collections import Counter
import hashlib
import json
import numpy as np
from PIL import Image
root = Path(__file__).resolve().parents[1]
results = {}
for path in sorted((root / 'referencias').glob('*.png')):
    im = Image.open(path)
    a = np.array(im.convert('RGBA'))
    rgb = a[:, :, :3]
    mask = ~((rgb[:, :, 0] > 220) & (rgb[:, :, 1] < 50) & (rgb[:, :, 2] > 220))
    def box(m):
        y, x = np.where(m)
        return [int(x.min()), int(y.min()), int(x.max()) + 1, int(y.max()) + 1]
    item = {'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'size': list(im.size), 'mode': im.mode,
            'alpha_values': np.unique(a[:, :, 3]).tolist(),
            'bbox_xyxy_exclusive': box(mask),
            'background_mode_rgb': list(Counter(map(tuple, rgb[~mask].tolist())).most_common(1)[0][0])}
    if path.name.startswith('Idle'):
        frames = []
        for r in range(2):
            for c in range(4):
                x, y = c * 362, r * 543
                frames.append({'frame': r * 4 + c + 1, 'cell_xywh': [x, y, 362, 543],
                               'bbox_local_xyxy_exclusive': box(mask[y:y+543, x:x+362])})
        item['frames'] = frames
    results[path.name] = item
out = {'method': 'Approximate foreground: NOT (R>220 AND G<50 AND B>220); zero-based coordinates, exclusive maxima.', 'sources': results}
(root / 'analise' / 'medicoes.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print('Medições gravadas para', len(results), 'fontes.')
