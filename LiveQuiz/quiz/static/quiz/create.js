var choiceCount = 1;
var questionCount = 1;
var limit = 4;

function addChoice(divName) {
    if (choiceCount == limit) {
        alert("Answer Choice limit reached");
    }
    else {
        var newdiv = document.createElement('div');
        newdiv.innerHTML = "Choice " + (choiceCount + 1) + " <input type='text' id='" + (choiceCount + 1) + "' name='answerChoices[]" + (questionCount) + "'>";
        document.getElementById(divName).appendChild(newdiv);
        choiceCount++;
    }
}

function addQuestion(divName) {
    if (choiceCount < 1) {
        alert("Please enter a choice");
    }
    else {
        choiceCount = 0;
        var newdiv = document.createElement('div');
        newdiv.innerHTML = "<br>Question " + (questionCount + 1) + "<input type='text' id='" + (questionCount + 1) + "' name='questions[]'>";
        document.getElementById(divName).appendChild(newdiv);
        questionCount++;
    }
}