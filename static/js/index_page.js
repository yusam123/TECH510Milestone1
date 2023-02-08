function showMessage1() {
    var x = document.getElementById("color_question");
    var name = document.getElementById("input").value;
    document.getElementById("color_label").innerHTML = "Hello, " + name + ". What is your favorite color?";
    x.style.display = "block";
 }
 function showMessage2() {
  var x = document.getElementById("age_question");
  var name = document.getElementById("input").value;
  document.getElementById("age_label").innerHTML = "Hello, " + name + ". How old are you?";
  x.style.display = "block";
}
function showMessage3() {
  var x = document.getElementById("time_question");
  var name = document.getElementById("input").value;
  document.getElementById("time_label").innerHTML = "Hello, " + name + ". when did you get up today?";
  x.style.display = "block";
}
 