# experiments for paperswan

Paper Swan will be a tool that will transform components (html files) into a big html and a big js file (aka bundle).

These two files will be lazy loaded by the main html file (index.html) that already has a bit of css and a bit of js in it for the stuff above the fold.

## why?

- we want to work in components, but we want to deliver bundles.
- we want to be fast for initial load (above the fold) and lazy load the rest
- we want to minify the css and js files so that they are small and can be cached.
- we want all the html to be present because we want SPA UX.

## how?

- right now python script. But we have to think about the whole developer journey.
- tailwind will take care of the css.
- we will do the tailwind of scripts by the transformations in the python script.

## ideas

How can we make this a good developer experience? How can we make it easy to use?

### templ and golang

We like golang. We like templ. Can we do something with that?

What if we did a templ file like this:

```templ
script home_script() {
    function say_hi() {
        console.log('Hi from home!');
    }
}
templ home(){
    <div id="home">
        <h1 onclick="say_hi()">Home</h1>
        <p>Welcome to the home page!</p>
    </div>
}
```

Then we could use home in our golang project for creating a bigger html file and have a separate function that just puts all the scripts together in a big js file.
