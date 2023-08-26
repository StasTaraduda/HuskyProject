let nextQuestion = document.getElementById("next_question")
let questions = document.querySelectorAll(".question")
let currentQuestion = 0
let res = []

questions[currentQuestion].style.display = "block"
for(let i =1; i<questions.length; i++){
    questions[i].style.display = "none"
}
nextQuestion.addEventListener("click", save)
function save(){
    questions[currentQuestion].style.display = "none"
    currentQuestion++

    var rad=document.getElementsByName('0');
    for (let i=0;i<rad.length; i++) {
        if (rad[i].checked) {
            res.push(i)
             break
            
        }
    }
    if(currentQuestion == questions.length){
        document.querySelector(".answer").style.display ="none"
        document.querySelector(".result").insertAdjacentHTML("beforeend",`
            <h1>Ваші відповіді</h1>
            <div class="question">Професіоналізм лікарів: ${res[0]}</div>
            <div class="question">Дієвість наданої допомоги: ${res[1]}</div>
            <div class="question">Дотримання санітарних норм: ${res[2]}</div>
            <div class="question">Якість надання різного типу послуг: ${res[3]}</div>
           `)
        var storage =JSON.parse(localStorage.getItem('opros')) 
        if(storage==null){
            storage = [res]
        }else{
            storage.push(res)
        }
        localStorage.setItem('opros', JSON.stringify(storage));
        document.querySelector('.exit').style.display = "block"
        nextQuestion.style.display = "none"
        var avr = Average(storage) 
        document.querySelector(".result").insertAdjacentHTML("beforeend",`
            <h1>Рейтинг</h1>
            <div class="question">Професіоналізм лікарів: ${avr[0]}</div>
            <div class="question">Дієвість наданої допомоги: ${avr[1]}</div>
            <div class="question">Дотримання санітарних норм: ${avr[2]}</div>
            <div class="question">Якість надання різного типу послуг: ${avr[3]}</div>
            `)
    }else{
        questions[currentQuestion].style.display = "block"

        if(currentQuestion==questions.length - 1){
            nextQuestion.innerText = "Зберегти"
            // currentQuestion++
    
        }
    }
    
}

function Average(storage){
    var res = []
    for(let i = 0; i <=storage[0].length; i++){
        res.push(0)
    }
    for(let i = 0;i<storage.length;i++){
        for(let j = 0; j< storage[i].length;j++){
            res[j]+=storage[i][j]
        }
    }
    for(let i = 0; i < storage[0].length; i++){
        res[i]/=storage.length
    }
    return res
}
