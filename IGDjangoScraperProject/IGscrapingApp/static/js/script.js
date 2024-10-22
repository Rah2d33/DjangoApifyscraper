//  document.querySelector('form').addEventListener('submit', function(event) {
//     event.preventDefault();

//     // This would normally trigger your backend call to scrape data
//     // For demonstration, we'll dynamically generate a table.

//     const tableData = [
//         { field: 'Username', value: 'demo_user' },
//         { field: 'Followers', value: '1,000' },
//         { field: 'Posts', value: '300' },
//     ];

//     const table = document.createElement('table');
//     const tableHead = `<tr><th>Field</th><th>Value</th></tr>`;
//     table.innerHTML = tableHead;

//     tableData.forEach(row => {
//         const tableRow = `<tr><td>${row.field}</td><td>${row.value}</td></tr>`;
//         table.innerHTML += tableRow;
//     });

//     document.getElementById('scraped-data').innerHTML = '';
//     document.getElementById('scraped-data').appendChild(table);
// });

// // =================================================

//     // Add event listener for the clear button to clear input in one click, even when typing
//     document.addEventListener('DOMContentLoaded', function() {
//         const inputField = document.getElementById('search');
//         const clearBtn = document.querySelector('.clear-btn');

//         // Show the clear button when there's text in the input field
//         inputField.addEventListener('input', function() {
//             if (inputField.value !== '') {
//                 clearBtn.style.display = 'block';
//             } else {
//                 clearBtn.style.display = 'none';
//             }
//         });

//         // Clear the input field on a single click
//         clearBtn.addEventListener('click', function() {
//             inputField.value = '';
//             inputField.focus();  // Focus back on the input field after clearing
//             clearBtn.style.display = 'none';  // Hide clear button after clearing
//         });

//         // Initially hide the clear button if input is empty
//         if (inputField.value === '') {
//             clearBtn.style.display = 'none';
//         }
//     });

//     document.getElementById('scrape-btn').addEventListener('click', async function() {
//         const username = document.getElementById('search').value;
//         if (!username) return alert('Please enter a username.');

//         const response = await fetch('/scrape', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify({ username })
//         });

//         const result = await response.json();
//         const resultsDiv = document.getElementById('results');

//         if (response.ok) {
//             resultsDiv.innerHTML = `
//                 <h3>Scraped Data:</h3>
//                 <p><strong>Username:</strong> ${result.scraped_data.username}</p>
//                 <p><strong>Display Name:</strong> ${result.scraped_data.display_name}</p>
//                 <p><strong>Bio:</strong> ${result.scraped_data.bio}</p>
//                 <p><strong>Profile URL:</strong> <a href="${result.scraped_data.profile_url}" target="_blank">${result.scraped_data.profile_url}</a></p>
//             `;
//         } else {
//             resultsDiv.innerHTML = `<p style="color: red;">${result.error}</p>`;
//         }
//     });

// Function to add the slide-in effect for h1
document.addEventListener("DOMContentLoaded", function() {
    const h1 = document.querySelector('h1');
    if (h1) {
        // Add the slide-in class after 500ms
        setTimeout(() => {
            h1.classList.add('slide-in');
        }, 500);  // Adjust delay as needed
    }
});

