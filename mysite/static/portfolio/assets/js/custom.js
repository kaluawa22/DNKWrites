$(function () {
  $(document).scroll(function () {
    var $nav = $(".navbar navbar-expand-lg");
    $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
  });
});