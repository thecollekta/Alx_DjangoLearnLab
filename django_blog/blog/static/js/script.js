// blog/static/js/script.js
// document.addEventListener('DOMContentLoaded', function() {
//     // Add a click event listener to all post titles
//     const postTitles = document.querySelectorAll('.post h2');
//     postTitles.forEach(title => {
//         title.addEventListener('click', function() {
//             // Toggle the visibility of the post content
//             const content = this.nextElementSibling;
//             if (content.style.display === 'none') {
//                 content.style.display = 'block';
//                 this.classList.add('active');
//             } else {
//                 content.style.display = 'none';
//                 this.classList.remove('active');
//             }
//         });
//     });

//     // Add a "Back to Top" button
//     const backToTopButton = document.createElement('button');
//     backToTopButton.innerText = 'Back to Top';
//     backToTopButton.style.position = 'fixed';
//     backToTopButton.style.bottom = '20px';
//     backToTopButton.style.right = '20px';
//     backToTopButton.style.display = 'none';
//     document.body.appendChild(backToTopButton);

//     backToTopButton.addEventListener('click', function() {
//         window.scrollTo({top: 0, behavior: 'smooth'});
//     });

//     window.addEventListener('scroll', function() {
//         if (window.pageYOffset > 100) {
//             backToTopButton.style.display = 'block';
//         } else {
//             backToTopButton.style.display = 'none';
//         }
//     });
// });