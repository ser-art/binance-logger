if [[ ! $(python -c 'import pkgutil; print(1 if pkgutil.find_loader("pytest") else 0)') ]]
then
    pip install pytest
fi

if [[ ! $(python -c 'import pkgutil; print(1 if pkgutil.find_loader("pytest-depends") else 0)') ]]
then
    pip install pytest-depends
fi

export $(grep -v '^#' config/.env | xargs)

export PYTHONPATH=$PWD

pytest -vs