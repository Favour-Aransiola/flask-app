from assignment import app
from flask import render_template
from assignment import listed_companies


@app.route('/companies')
def companies():
    companies=listed_companies [['Company Name', 'Job Title', 'Location']]
    comp_list=[]
    for i,comp in enumerate(companies.iloc):
        comp_list.append([i+1,comp['Company Name'], comp['Job Title'], comp['Location']])
    return render_template('companies.html', companies= comp_list)

@app.route('/categories')
def categories():
    categories=listed_companies [['Company Name', 'Job Title','Salary']]
    comp_list=[]
    for i,comp in enumerate(categories.iloc):
        comp_list.append([i+1,comp['Company Name'], comp['Job Title'],comp['Salary'][1:-3]])
    return render_template('categories.html', categories= comp_list)


@app.route('/')
@app.route('/overview')
def overview():
    overview=listed_companies [['Company Name', 'Job Title', 'Salary', 'Salaries Reported','Location']]
    comp_list=[]
    for i,comp in enumerate(overview.iloc):
        comp_list.append([i+1,comp['Company Name'], comp['Job Title'], comp['Salary'][1:-3], comp['Salaries Reported'],comp['Location']])
    return render_template('overview.html', overview= comp_list)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('page_not_found.html')