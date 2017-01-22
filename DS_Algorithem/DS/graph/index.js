/*顶点*/
function Vertex(name, wasVisited) {
    this.name = name;
    this.wasVisited = wasVisited;
}

/*图*/
function Graph(v) {
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
function addEdge(v, w) {
    this.adj[v].push(w);
    this.adj[w].push(v);
    this.edges++;
}

/*打印图*/
function showGraph() {
    for (var i = 0; i < this.vertices.length; i++) {
        console.log(i + " > ");
        for (var j = 0; j < this.vertices.length; j++) {
            if (this.adj[i][j] != undefined) {
                console.log(j)
            }
        }
    }
}

/* 搜索图 */
this.marked = [];
for (var i = 0; i < this.vertices.length; i++) {
  this.marked[i] = false;
}
function dfs(v){
  this.marked[v] = true;
  if( this.adj[v] != undefined ){
    print("当前顶点:" + v);
  }
  for each(var w in this.adj[v]){
    if(!this.marked[w]){
      this.dfs(w);
    }
  }
}

/* 广度优先搜索 */
function bfs(s){
  var queue = [];
  this.marked[s] = true;
  queue.push(s); // 添加到対尾
  while( queue.length > 0 ){
    var v = queue.shift();
    if( v == undefined ){  // 这该是 !==
        console.log("node:"+v);
    }

    for each(var w in this.adj[v]){
      if(!this.marked[w]){
        this.edgeTo[w] = v;
        this.marked[w] = true; // 这句话有必要么
        queue.push(w);
      }
    }
  }
}

/* 查找最短路径 */
this.edgeTo =[];
function bfs(s){
  var queue = [];
  this.marked[s] = true;
  queue.push(s);
  while(queue.length > 0){
    var v = queue.shift();
    if(v == undefined){
      console.log("node",v);
    }
    for each(var w in this.adj[v]){
      if(!this.marked[w]){
        this.edgeTo[w] = v;
        this.marked[w] = true;
        queue.push(w);
      }
    }
  }
}
