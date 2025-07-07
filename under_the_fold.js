(function init_under_the_fold () {
    'use strict';
    const fold = document.querySelector('#fold');
    // fetch "under_the_fold.html" and insert it into the fold element
    fetch('under_the_fold.html')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(html => {
            fold.outerHTML = html;
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
})();
