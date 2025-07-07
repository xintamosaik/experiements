(function init_under_the_fold () {
    'use strict';
    
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'under_the_fold.css';
    document.head.appendChild(link);

    fetch('under_the_fold.html')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(html => {
            document.querySelector('#fold').outerHTML = html;
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
})();
