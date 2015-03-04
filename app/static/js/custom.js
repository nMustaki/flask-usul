/* global $ */

$( document ).ready(function() {
    "use strict";

    // For IE
    if (navigator.userAgent.match(/IEMobile\/10\.0/)) {
      var msViewportStyle = document.createElement('style');
      msViewportStyle.appendChild(
        document.createTextNode(
          '@-ms-viewport{width:auto!important}'
        )
      );
      document.querySelector('head').appendChild(msViewportStyle);
    }
    var nua = navigator.userAgent;
      var isAndroid = (nua.indexOf('Mozilla/5.0') > -1 && nua.indexOf('Android ') > -1 && nua.indexOf('AppleWebKit') > -1 && nua.indexOf('Chrome') === -1);
      if (isAndroid) {
        $('select.form-control').removeClass('form-control').css('width', '100%');
      }

    // Home : universe selection on hover or touch (select)
    var universe_url = [
        "/static/images/cashpad/Cashpad-140-16-9_720p.jpg",
        "/static/images/cashpad/Cashpad-033-16-9_720p.jpg",
        "/static/images/cashpad/Cashpad-065-16-9_720p.jpg",
        "/static/images/cashpad/Cashpad-159-16-9_720p.jpg",
        "/static/images/cashpad/Cashpad-097-16-9_720p.jpg",
        "/static/images/cashpad/Cashpad-120-19-9_720p.jpg"
    ];
    $(".home-btn-universe .universe-btn-container").on("mouseover", function(e) {
        var pos = $(e.currentTarget).data("url");
        $(".home-universe img").attr("src", universe_url[pos]);
        $(".home-btn-universe .active").removeClass("active");
        $("#universe-" + pos).addClass("active");
    });
    $(".home-btn-universe-select select").on("change", function(e) {
        var pos = this.value;
        $(".home-universe img").attr("src", universe_url[pos]);
        $(".home-btn-universe .active").removeClass("active");
        $("#universe-" + pos).addClass("active");
    });
    $("#home-reasons-carousel").carousel({
        interval:false
    });
});
