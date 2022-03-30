import requests
import typer

app = typer.Typer()

@app.command()
def format(sql: str = typer.Argument(..., help = "Your SQL query to be formatted, remember to pass it into quotes(single or double)")):
    """
        Format your single line SQL Query into Multi-line SQL
    """
    sql_formated = api_call(sql)
    typer.echo(f"\n{sql_formated}")

def api_call(sql : str):
    url = "https://sqlformat.org/api/v1/format"
    params = {
        'sql' : f'{sql}',
        'reindent'       : '1',
        'indent_width'   : '3',
        'keyword_case'   : 'upper',
        'strip_comments' : '1'}
    response =  requests.post(url, data = params)
    result = response.json()['result']
    return result

#if __name__ == "__main__":
#    app()
