$(document).ready(function () {
  // display mesasge
  eel.expose(Displaymessage)
  function Displaymessage(message) {
    $(".siri-message li:first").text(message);
    $('.siri-message').textillate('start');
  }
// display container

  eel.expose(showcontainer)
  function showcontainer(){
    $("#body").attr("hidden",false);
    $("#siriwave").attr("hidden",true);
  }

});
