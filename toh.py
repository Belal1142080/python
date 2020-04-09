public void bfs()
{
    //BFS uses Queue
    Queue q=new LinkedList();
    q.add(this.rootNode);
    printNode(this.rootNode);
    rootNode.visited=true;
    while(!q.isEmpty())
    {
        Node n=(Node)q.remove();
        Node child=null;
        while((child=getUnvisitedChildNode(n))!=null)
        {
            child.visited=true;
            printNode(child);
            q.add(child);
        }
    }
    //Clear visited property of nodes
    clearNodes();
}



public class Hanoi {
public static void hanoi(int n, String from, String temp,
String to) {
if (n == 0) return;01
hanoi(n-1, from, to, temp);
System.out.println("Move disc " + n +
" from " + from + " to " + to);
hanoi(n-1, temp, from, to);
}

N = Integer.parseInt(args[0]);
hanoi(N, "A", "B", "C");
}
