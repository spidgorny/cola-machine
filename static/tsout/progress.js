document.addEventListener('DOMContentLoaded', () => {
   const links = document.querySelectorAll('a')
   Array.from(links).map(a => {
       // console.log(a);
       a.addEventListener('click', (e) => {
           e.preventDefault();
           // console.log(e.target);
           const popup = document.querySelector('#popup');
           popup.classList.remove('hidden');

           // "/cola/10"
           let link = e.target.closest('a');
           let href = link.getAttribute('href');
           console.log(link, href);
           const seconds = parseInt(href.split('/')[2], 10);
           console.log(seconds);
           let value = 0;
           const progress = popup.querySelector('progress');
           const timer = setInterval(() => {
               value += 100 / seconds / 1000 * 16;
               progress.setAttribute('value', value);
           }, 16);
           fetch(a.getAttribute('href'));
           setTimeout(() => {
               clearInterval(timer);
               popup.classList.add('hidden');
           }, seconds * 1000);
       })
   })
});