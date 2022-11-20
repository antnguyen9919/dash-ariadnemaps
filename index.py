from dash import dcc,html

from dash.dependencies import Input,Output

#Connect to main app.py file 
# from app import app 
from app import server 
from apps import vgames,global_sales 

app.layout=html.Div([html.Div([
    dcc.Link("Video Games|",href="/apps/vgames"),
    dcc.Link("Other Products",href="/apps/global_sales"),
], className="row"),
dcc.Location(id="url",refresh=False),
html.Div(id="page-content",children=[])

])


@app.callback(
    Output(component_id='page-content',component_property='children'),
    [Input(component_id='url',component_property='pathname')]
)
def display_page(pathname):
    if pathname=="/":
        return html.Div([html.H1(["Welcome"])])
    if pathname == "/apps/vgames":
        return vgames.layout
    if pathname == "/apps/global_sales":
        return global_sales.layout
    else:
        return "404 Page Error! Please choose a Link"

if __name__=='__main__':
    app.run_server(debug=True)        
