
/************************************************************************
* Author:
*    Michael Mann 
*
* Description:
*    File supports the functionality of the TRC HTML/JS/CSS Excercise
************************************************************************/

// event handler for the change/click of a check box
// if the box is checked we strikethrough the content in the Task Name column and add a completed date
const modifyTask = (e) => {
    if (e.target.checked) {

        // formatted date to be placed in the Time Completed column
        const completeDate = new Date().toLocaleString(undefined, {
            day: 'numeric',
            month: 'short',
            year:'numeric',
            hour: '2-digit',
            minute:'2-digit'
        })

        // data cell containing check box
        parentCell = e.target.parentNode

        // the previous element is our time complete column, place the completed date in cell
        parentCell.previousElementSibling.innerHTML = completeDate

        // the cell back two from parent is our task name column, strikethrough the task
        textCell = parentCell.previousElementSibling.previousElementSibling
        textCell.style.textDecoration = 'line-through'
    }
    else {
        
        // the data cell the checkbox is in
        parentCell = e.target.parentNode
        
        // the previous element is our time cell, blank out the completed date
        parentCell.previousElementSibling.innerHTML = ''

        // element two back from parent is our task name column, remove the strikethrough
        textCell = parentCell.previousElementSibling.previousElementSibling
        textCell.style.textDecoration = 'initial'
    }
}

// funtion adds a task to our todo table
const addTodo = (todoItem) => {
    const newRow    = document.createElement('tr')
    const taskCell  = document.createElement('td')
    const timeCell  = document.createElement('td')
    const chbxCell  = document.createElement('td')
    const checkBox  = document.createElement('input')

    // set the text content of our first cell 
    taskCell.innerHTML = todoItem

    // set up the final cell containing the check box
    checkBox.setAttribute('type', 'checkbox')
    chbxCell.appendChild(checkBox)
    chbxCell.className = 'item_complete'              
    chbxCell.addEventListener('change', modifyTask)    // add the event listener for our checkboxes   

    // add the newly created table cells to the new table row
    newRow.appendChild(taskCell)
    newRow.appendChild(timeCell)
    newRow.appendChild(chbxCell)

    // find the table and add our row to it
    const tbl = document.getElementById('todo')
    tbl.appendChild(newRow)
}


// listen for the button click
document.querySelector('button').addEventListener('click', function(){
    const userInput = document.getElementById('myInput').value

    if (userInput !== '') {
    addTodo(userInput)
    }

})

// listen for enter key while in the input field
document.getElementById('myInput').addEventListener("keyup", function(e) {
    e.preventDefault();
    if (e.keyCode === 13) {
        document.querySelector('button').click();
    }
})


// find all of the existing checkboxes in our item_complete table cells and set event listener
let checkBoxes = document.querySelectorAll('.item_complete')
checkBoxes.forEach(cbox => cbox.addEventListener('change', modifyTask))
