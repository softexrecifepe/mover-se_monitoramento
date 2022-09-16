$(document).ready(function(){
    
    console.log("teste1");
    $('#jsonDiv').attr("hidden", true);

    $('#thinkspeakLoadBtn').click( function(){
        console.log("teste3");        

        let channel_val = $('#channel-id').val()
        if (channel_val){
            $.ajax({
                type : 'GET',
                url : 'https://api.thingspeak.com/channels/'+ channel_val +'/feeds.json?results=2',
                //data : { station : $('#search-form').val()},
                success : function(response) {  
                    console.log(response);
                    pretty = JSON.stringify(response, undefined, 4)
                    $('#jsonThinkspeak').val(pretty);
                    $('#jsonDiv').attr("hidden", false);
                },
                error : function(response){
                    alert(response.error);        
                }
            })
        }else{
            console.log("sem channel");
        }
    });
    
    
    $('#thinkspeakCleanBtn').click( function(){
        $('#channel-id').val('')
        $('#jsonDiv').attr("hidden", true);
    });
            
});
