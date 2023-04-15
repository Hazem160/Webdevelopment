

document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');

  // Sends values in composed email to server side in /emails path, then loads to "sent" view
  document.querySelector("#compose-form").onsubmit = function () {
    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
          recipients: document.querySelector("#compose-recipients").value,
          subject: document.querySelector("#compose-subject").value,
          body: document.querySelector("#compose-body").value
      })
    })
    .then(load_mailbox('sent'));
    return false;
  }

});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  //  every email in the array taken from "emails/<str:mailbox>" is converted into json form
  // then a div element is added into "emails-view" with the content of email

    fetch (`emails/${mailbox}`).then(emails => emails.json()).then(emails => {
      emails.forEach(email => {

        const element = document.createElement('div');
        element.innerHTML = `<h4><b>${email.sender}</b>   ${email.body} <span class="span">${email.timestamp}<span></h4>`;
        element.addEventListener("click", () => view_mail(email.id));
        if (email.read === true) {
          element.classList.add("div");
          
        }
        document.querySelector('#emails-view').append(element);
        
        // Add button to archive or undo it depending on if user is in "mailbox/inbox" or "mailbox/archive"
        // if button is clicked, then it will respectively change archived field in json to true and false

        if (mailbox === "inbox"){
        const button = document.createElement('button');
        button.innerHTML = "Archive";
        button.classList.add("btn","btn-sm","btn-outline-primary","color");
        element.append(button);
        button.onclick = () =>{
          fetch(`emails/${email.id}`, {
            method: 'PUT',
            body: JSON.stringify({
                archived: true
            })
          })
        }
      }
        else if (mailbox === "archive") {
          const button = document.createElement('button');
          button.innerHTML = "Unarchive";
          button.classList.add("btn","btn-sm","btn-outline-primary","color");
          element.append(button);
          button.onclick = () => {
            fetch(`emails/${email.id}`, {
              method: 'PUT',
              body: JSON.stringify({
                  archived: false
              })
            })
          }
        }
        
      })
    
    })
  
}
// if user clicks on any email in inbox, archive or sent, it will display only that email

function view_mail(mail_id){
  fetch(`emails/${mail_id}`).then(response => response.json())
  .then(email => {
    
    const element = document.createElement('div');
    element.innerHTML = `<h4><b> From:</b> ${email.sender}</h4>
    <h4><b> To:</b> ${email.recipients}</h4>
    <h4><b> Subject:</b> ${email.subject}</h4>
    <h4><b> Timestamp:</b> ${email.timestamp}</h4>`;

    const body = document.createElement('div');
    body.innerHTML = `<h2>${email.body}</h2>`;
    body.classList.add("margin");

    // adding button for replying and if clicked, it will display the compose page with
    // pre-filled recipients, subject and body fields. Ultimately, it will set the read field in json to
    // true through PUT request

    document.querySelector('#emails-view').innerHTML = " ";
    button = document.createElement("button");
    button.innerHTML = "Reply";
    button.classList.add("btn","btn-sm","btn-outline-primary");
    button.onclick = function() {
      compose_email();
      document.querySelector('#compose-recipients').value = email.recipients;
      document.querySelector('#compose-subject').value = `Re: ${email.subject}`;
      document.querySelector('#compose-body').value = `On ${email.timestamp}, ${email.sender} wrote: ${email.body}`;
    }
    document.querySelector('#emails-view').append(element,button,body);
    
  })
  .then(fetch(`emails/${mail_id}`, {
    method: 'PUT',
    body: JSON.stringify({
        read: true
    })
  }))
}