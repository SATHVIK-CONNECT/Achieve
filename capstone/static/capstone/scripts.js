// function preventBack() {
//   window.history.forward();
// }
// setTimeout("preventBack()", 0);
// window.onunload = function () {
//   null;
// };

// window.addEventListener("beforeunload", (event) => {
//   event.preventDefault();
//   event.returnValue = "Are you sure?";
// });

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length == 2) return parts.pop().split(";").shift();
}

function btnhandler(id, ch, usersquiz) {
  var choice = document.getElementById(`choice_${id}`);
  choice.style.display = "flex";
  var option = document.getElementById(`option_${id}`);
  document.querySelectorAll(".inp").forEach((inp) => {
    if (inp.checked) {
      var value = inp.value;
      if (value == ch) {
        option.innerHTML = "You chose: Correct";
        var scr = document.getElementById(`score_${usersquiz}`);
        var val = parseInt(scr.innerHTML);
        fetch(`/correction/${usersquiz}`, {
          method: "POST",
          headers: { "Content-type": "application/json", "x-CSRFToken": getCookie("csrftoken") },
          body: JSON.stringify({
            score: val + 1,
          }),
        })
          .then((response) => response.json())
          .then((result) => {
            scr.innerHTML = result.data;
          });
      } else if (value != ch) {
        option.innerHTML = "You chose: Wrong";
      }
    }
  });
}

function submission(id, ch) {
  document.querySelectorAll(".inp").forEach((inp) => {
    if (inp.checked) {
      var value = inp.value;
      if (value == ch) {
        var scr = document.getElementById(`score_${id}`);
        var val = parseInt(scr.innerHTML);
        fetch(`/submission/${id}`, {
          method: "POST",
          headers: { "Content-type": "application/json", "x-CSRFToken": getCookie("csrftoken") },
          body: JSON.stringify({
            score: val + 1,
          }),
        })
          .then((response) => response.json())
          .then((result) => {
            scr.innerHTML = result.data;
          });
      } else {
        var scr = document.getElementById(`score_${id}`);
        var val = parseInt(scr.innerHTML);
        fetch(`/submission/${id}`, {
          method: "POST",
          headers: { "Content-type": "application/json", "x-CSRFToken": getCookie("csrftoken") },
          body: JSON.stringify({
            score: val,
          }),
        })
          .then((response) => response.json())
          .then((result) => {
            scr.innerHTML = result.data;
          });
      }
    }
  });
}

document.getElementById("createQuizBtn").addEventListener("click", (event) => {
  document.getElementById("createQuiz").style.display = "block";
});

document.getElementById("createQuestionBtn").addEventListener("click", (event) => {
  document.getElementById("createQuestion").style.display = "block";
});
