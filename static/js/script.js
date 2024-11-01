document.addEventListener("DOMContentLoaded", function() {
  setTimeout(function() {
    let alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
      alert.classList.remove('show');
      alert.classList.add('fade');
      setTimeout(function() {
        alert.classList.add('hide');
      }, 600);
    });
  }, 3000);
});