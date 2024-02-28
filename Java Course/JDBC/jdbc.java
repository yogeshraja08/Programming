// This code is for establishing connection with MySQL
// database and retrieving data
// from db Java Database connectivity

/*
*1. import --->java.sql
*2. load and register the driver ---> com.jdbc.
*3. create connection
*4. create a statement
*5. execute the query
*6. process the results
*7. close
*/

import java.sql.*;

class jdbc {
	public static void main(String[] args) throws Exception
	{
		String url = "jdbc:mysql://localhost:3306/user"; // table details
		String username = "root"; // MySQL credentials
		String password = "";
		String query = "select *from students"; // query to be run
		Class.forName("com.mysql.cj.jdbc.Driver"); // Driver name
		Connection con = DriverManager.getConnection(url, username, password);
		System.out.println("Connection Established successfully");
		Statement st = con.createStatement();
		ResultSet rs = st.executeQuery(query); // Execute query
		rs.next();
		String name = rs.getString("name"); // Retrieve name from db
		System.out.println(name); // Print result on console
		st.close(); // close statement
		con.close(); // close connection
		System.out.println("Connection Closed....");
	}
}