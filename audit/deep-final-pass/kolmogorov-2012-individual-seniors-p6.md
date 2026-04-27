# Kolmogorov 2012 Individual Seniors P6

Verdict: `ai_checked`.

I found the official source in the current Kolmogorov archive:

- archive index: `https://turmath.ru/kolm/archive.php`
- downloaded archive: `https://turmath.ru/kolm/files/archive/kolm16.zip`
- source file inside archive: `kolm16/lichol16.doc`

The local `tmp/kolm12` directory was not the needed 2012 material: it contains XII Cup / 2008 files. The official XVI Cup archive contains `lichol16.doc`, whose personal seniors solution block includes this problem.

Recovered proof content:

- the answer is `100(2n^2 - 2n + 4)`;
- the lower bound uses the diagonal cuts `x+y=k+1/2`;
- the first pass gives one missed edge on each of `2n` cuts;
- the refined even-cut argument gives two additional missed edges on each of `(n-2)/2` lower-left cuts and `(n-2)/2` upper-right cuts, for a total of `4n-4`;
- the official construction deletes exactly `(n-1)+(3n-9)+6 = 4n-4` unit edges using the listed boundary edges and short boundary paths;
- I checked the construction as an oriented grid for small even `n = 4,6,8,10,12`: the remaining graph has exactly the Euler-trail degree imbalance at `(0,0)` and `(n,n)` and is weakly connected.

Changed YAML:

- expanded the compressed solution into a self-contained proof;
- set the relevant statement/profile/idea/solution/editorial statuses to `ai_checked`;
- changed `repair_status` to `repaired_full_solution_from_official_archive`;
- recorded the official archive lookup in editorial notes.

Validation:

- `python tools/validate.py`
- `python tools/check_links.py`
