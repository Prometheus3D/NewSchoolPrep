
function sendProbNum() {
    var question_num = document.getElementById('add_questions').value;
    $.ajax({
        url: '/math/addition/start',
        contentType: "application/json;charset=UTF-8",
        dataType: 'json',
        data: JSON.stringify({question_num}),
        type: 'POST',
        success: function(response) {
            alert("Message Received");
            console.log(response);


        },
        error: function(data) {
            $("#body-content").text(data.result);
            console.log(data);
        }
    });
}

function sendNums() {
        var question_num = document.getElementById('add_questions').value;
        var num_sub = document.getElementById('num-sub');
        var i = Integer.parseInt(question_num);
        num_sub.setAttribute('action', i)


}