#from flask import render_template,request,redirect,url_for
#from . import main
#from flask import render_template,request,redirect,url_for
#from ..request import get_source,article_source,get_category,get_headlines
from turtle import title
from flask import render_template
from . import main
from ..request import get_sources, get_articles
from ..model_sources import Source 

#Views
@main.route('/')  #Route defining the view function.
def index():
    '''
    Root function returning index/home page with data
    '''
#Getting the popular categories    
    general = get_sources('general')
    sports = get_sources('sports')
    business = get_sources('business')
    technology = get_sources('technology')
    entertainment = get_sources('entertainment')
    science = get_sources('science')

    title = 'You Have Landed on the Best Site To Get the Latest News & Updates.'

    return render_template('index.html', title=title, general=general, sports=sports, business=business, technology=technology, entertainment=entertainment, science=science) 

@main.route('/<source_id>')
def articles(source_id):

    '''
    View article page function that returns the various article details page and its data
    '''
    news_source = get_articles(source_id)
    title = f'Welcome to {source_id}'
    return render_template('news.html', title=title, name = source_id, news = news_source)
    