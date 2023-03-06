const  quizForm = document.getElementById("quiz-form");
let cookie = document.cookie
let csrfToken = cookie.substring(cookie.indexOf('=') + 1)
// function submitform(){

// }

quizForm.addEventListener('submit', e=>{
    e.preventDefault();
    console.log("OK");
    const ans = document.getElementsByClassName("answers");
    var data = {}
    // console.log(ans);
    Array.from(ans).forEach(element => {
        // console.log(element);
        if (element.checked){
            console.log(element.name, element.value);
            data[element.name] = element.value;
        }else{
            if (!data[element.name]) {
                data[element.name] = null
            }
        }
    });
    console.log(data);
    // const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    // data['csrfmiddlewaretoken']= '{% csrf_token %}';
    $.ajax({
        type: 'POST',
        url: window.location.href+'save_quiz/',
        headers: {'X-CSRFToken': csrfToken},
        data: data,
        success: function(response){
            console.log("ALL OK");
            console.log(response);
            alert(response['message']);
        }
    });
});