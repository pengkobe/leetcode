/*顶点*/
function Vertex(name, wasVisited){
  this.name = name;
  this.wasVisited = wasVisited;
}

/*图*/
function Graph(v){
  this.vertices = v;
  this.edges = 0;
  this.adj = [];
  for (var i = 0; i < this.vertices; i++) {
    this.adj[i] = [];
  }
  this.addEdge = addEdge;
  this.showGraph = showGraph;
}

/* 添加边 */
function addEdge(v,w){
 this.adj[v].push(w);
 this.adj[w].push(v);
 this.edges++;
}

/*打印图*/
function showGraph(){
    for (var i = 0; i < this.vertices.length; i++) {
       console.log(i +" > ");
      for (var j = 0; j < this.vertices.length; j++) {
        if(this.adj[i][j] != undefined){
           console.log(j)
        }
      }
    }
}
