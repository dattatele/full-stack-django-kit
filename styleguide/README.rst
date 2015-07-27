===========
Style Guide
===========

Serves as a single source of truth for all HTML, CSS, and HTML. Use this to create the required styles for the site.
It should be easy for non-django developers to work within this repo.

* Jinja - Using Jinja to create sample pages to preview html/css/js changes withing templates

Gulp Tasks
----------

::

    gulp build               Builds all and saves to dist/styleguide (CSS, JS, Jinja)
    gulp watch               Watches for any changes to css/js/html pages for auto rebuilds

Directory Layout
----------------

::

    └── dist
    └── src
        ├── js             # all *.js files will be consolidated and minified to dist/styleguide/js/site.js
        │   └── common.js
        ├── less           # main.less used to create dist/styleguide/css/site.js
        │   ├── layout.less
        │   └── main.less
        ├── pages          # sample pages and components of html pages
        │   ├── component.html
        │   └── index.html
        └── templates      # primary layouts for jinja
            └── layout.html

-----
Notes
-----

* **TODO** Create as separate repo.