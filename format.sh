set -x
set -e

isort --recursive  --force-single-line-imports --apply app*/
autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place app*/ --exclude=__init__.py
isort --multi-line=3 --trailing-comma --force-grid-wrap=0 --combine-as --line-width 88 --recursive --apply app*/
black app*/