cd stone/
python -m stone.cli python_types ../bosta ../spec/*.stone -a url_param -a query_params -a has_body
python -m stone.cli python_client ../bosta ../spec/*.stone -a url_param -a query_params -a has_body -- -m base -c BostaBase -t bosta
cd ..
