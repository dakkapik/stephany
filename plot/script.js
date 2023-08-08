TESTER = document.getElementById('tester');
TESTER2 = document.getElementById('test2');

Plotly.newPlot( TESTER, [{
x: [1, 2, 3, 4, 5],
y: [1, 2, 4, 8, 16] }], {
margin: { t: 0 } } );


Plotly.newPlot( TESTER2, [{
x: [1, 2, 3, 4, 5],
y: [1, 2, 4, 8, 70] }], {
margin: { t: 0 } } );