.PHONY: clean test package

clean:
	rm -rf build dist exchangeratesapi.egg-info .pytest_cache .coverage

test:
	pytest --cov-report term-missing --cov=exchangeratesapi tests/

package:
	python setup.py sdist bdist_wheel