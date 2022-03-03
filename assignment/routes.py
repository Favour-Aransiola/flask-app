from assignment import app
from flask import render_template
from assignment import listed_companies


@app.route('/companies')
def companies():
    companies=listed_companies [['ref', 'company_name', 'symbol']]
    comp_list=[]
    for i,comp in enumerate(companies.iloc):
        comp_list.append([i+1,comp['ref'], comp['company_name'], comp['symbol']])
    return render_template('companies.html', companies= comp_list)

@app.route('/categories')
def categories():
    categories=listed_companies [['company_name', 'symbol', 'category','category_number']]
    comp_list=[]
    for i,comp in enumerate(categories.iloc):
        comp_list.append([i+1,comp['company_name'], comp['symbol'], comp['category'], comp['category_number']])
    return render_template('categories.html', categories= comp_list)

@app.route('/shares')
def shares():
    shares=listed_companies [['ref', 'symbol', 'shares']]
    comp_list=[]
    for i,comp in enumerate(shares.iloc):
        comp_list.append([i+1,comp['ref'], comp['symbol'], comp['shares']])
    return render_template('shares.html', shares= comp_list)

@app.route('/')
@app.route('/overview')
def overview():
    overview=listed_companies [['ref', 'company_name', 'symbol', 'category_number','category','shares']]
    comp_list=[]
    for i,comp in enumerate(overview.iloc):
        comp_list.append([i+1,comp['ref'], comp['company_name'], comp['symbol'], comp['category'],comp['category_number'],comp['shares']])
    return render_template('overview.html', overview= comp_list)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('page_not_found.html')