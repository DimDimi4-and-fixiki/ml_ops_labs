# ml-ops-labs

Project is located inside `ml_ops_labs dir`

**How to run:**  

0) (Not necessary) For fast setup install [rye](https://rye.astral.sh/guide/installation/)
1) Install deps: `pip install .` or `rye sync`
2) locally install `postgresql`
3) For convenient commands if not using `rye`: `pip install poethepoet` 
4) Run DB: `poe run db-up` or `docker-compose -f docker-compose-local.yaml up`
5) Run web-app: `poe run web-view` or `streamlit run src/ml_ops_labs/web_view/index.py`

