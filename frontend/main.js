$(document).ready(function () {
    $('.text').textillate({
        loop:true,
        sync:true,
        in:{
            effect:"bounceIn",
        },
        out:{
            effect:"bounceOut"

        },
    });
    //siri config
     var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 740,
    height: 250,
    style:"ios9",
    amplitude:"1.5",
    speed:"0.25",
    auttostart:true
  });
  //siri message
  $('.siri-message').textillate({
        loop:true,
        sync:true,
        in:{
            effect:"fadeInUp",
            sync:true
        },
        out:{
            effect:"fadeOutUp",
            sync:true

        },
    })
    // mic handler
    $("#mic").click(function () { 
        eel.micsound()
        $("#body").attr("hidden", true);
         $("siriwave").attr("hidden", false);
         eel.allCommands()()

        
    });
});