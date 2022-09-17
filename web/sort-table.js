// sample table data from issue ticket

let table = [
    {
       name: 'Berekusu1',
       algorithms: 21,
       scripting: 45,
       sql: 3,
       total: 78
    },
     {
       name: 'Berekusu2',
       algorithms: 27,
       scripting: 9,
       sql: 6,
       total: 45
    },
     {
       name: 'Berekusu3',
       algorithms: 18,
       scripting: 1,
       sql: 0,
       total: 18
    },
]


// declare variables
let total_scores = [];
let algorithm_scores = [];
let scripting_scores = [];
let sql_scores = [];
let total_scores_sorted_table = [];
let algorithm_scores_sorted_table = [];
let scripting_scores_sorted_table = [];
let sql_scores_sorted_table = [];

// put each scores into different arrays
table.forEach(team => {
    total_scores.push(team.total)
    algorithm_scores.push(team.algorithms)
    scripting_scores.push(team.scripting)
    sql_scores.push(team.sql)
})

// sort the arrays in descending order
let total_scores_sorted = total_scores.sort(function(a, b){return b-a});
let algorithm_scores_sorted = algorithm_scores.sort(function(a, b){return b-a});
let scripting_scores_sorted = scripting_scores.sort(function(a, b){return b-a});
let sql_scores_sorted = sql_scores.sort(function(a, b){return b-a});


// sorting by total scores
total_scores_sorted.forEach(score => {
    table.forEach(team => {
        if (score === team.total) {
            total_scores_sorted_table.push(team);
        }
    })
})

console.log("\nSort by total scores: \n");
console.log(total_scores_sorted_table);


// sorting by algorithm scores
algorithm_scores_sorted.forEach(score => {
    table.forEach(team => {
        if (score === team.algorithms) {
            algorithm_scores_sorted_table.push(team);
        }
    })
})

console.log("\nSort by algorithm scores: \n");
console.log(algorithm_scores_sorted_table)


// sorting by scripting scores
scripting_scores_sorted.forEach(score => {
    table.forEach(team => {
        if (score === team.scripting) {
            scripting_scores_sorted_table.push(team);
        }
    })
})

console.log("\nSort by scripting scores: \n");
console.log(scripting_scores_sorted_table)


// sorting by sql scores
sql_scores_sorted.forEach(score => {
    table.forEach(team => {
        if (score === team.sql) {
            sql_scores_sorted_table.push(team);
        }
    })
})

console.log("\nSort by sql scores: \n");
console.log(sql_scores_sorted_table)    


