function showMessage1() {
    var x = document.getElementById("color_question");
    var name = document.getElementById("input").value;
    document.getElementById("color_label").innerHTML = "Hello, " + name + ". What is your favorite color?";
    x.style.display = "block";
 }
 function showMessage2() {
  var x = document.getElementById("age_question");
  var name = document.getElementById("input").value;
  document.getElementById("age_label").innerHTML = "Hello, " + name + ". How old are you(please enter only number)?";
  x.style.display = "block";
}
function showMessage3() {
  var x = document.getElementById("time_question");
  var name = document.getElementById("input").value;
  document.getElementById("time_label").innerHTML = "Hello, " + name + ". When did you get up today(please enter only number, for example: 8)?";
  x.style.display = "block";
}
 