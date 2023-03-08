let btn = document.getElementById('btn')

btn.addEventListener('click',(e)=>{
    console.log('clicked')
    e.preventDefault()
    let boy = document.getElementById('boy').value
    let girl = document.getElementById('girl').value
    let result = document.getElementsByClassName('result')[0]
    let boy_sum=0
    let girl_sum=0
    for(let i = 0;i<boy.length;i++){
        const t=i
        let code = (boy[t]).charCodeAt(0)
        if(code>=65 && code<=90){
            boy_sum += (code+32)
        }
        else if(code>=97 && code<=122){
            boy_sum += code
        }
        else{
            boy_sum += 0
        }
    }
    for(let i = 0;i<girl.length;i++){
        const t=i
        let code = (girl[t]).charCodeAt(0)
        if(code>=65 && code<=90){
            girl_sum += (code+32)
        }
        else if(code>=97 && code<=122){
            girl_sum += code
        }
        else{
            girl_sum += 0
        }
    }
    let love = (boy_sum+girl_sum)%101
    result.innerHTML = `<p>Love percentage is ${love}%</p>`
    if(love>80){
        result.innerHTML += `<p>Perfect match</p>`
    }
    else if(love>60){
        result.innerHTML += `<p>Good match</p>`
    }
    else if(love>40){
        result.innerHTML += `<p>Not bad</p>`
    }
    else if(love>20){
        result.innerHTML += `<p>Not good</p>`
    }
    else{
        result.innerHTML += `<p>Not a match</p>`
    }
})