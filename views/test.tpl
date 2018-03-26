%#template for test function
<meta carset="utf-8">
    <title>TEST</title>
    <table border ="6">
    <th>Chore</th>
    <th>Person</th>
    <th>Status</th>
    <th>Option</th>
    <form action="/" method="GET">

    <tr>
        <td><input type="text" name="chore" placeholder="chore"></td>
        <td><input type="text" name="person" placeholder="person"></td>
        <td>
            <select name="status">
                <option value= "1">complete</option>
                <option value= "57">incomplete</option>
            </select>
        </td>
        <td>
            <button type="submit" name="submit" value="submit">
                <image src="../static/add.svg"></image>
            </button>
        </td>
    </tr>




    %for row in rows:
    <tr>
        <td>{{row['desk']}}</td>
        <td>{{row['person']}}</td>

        %if row['status'] == "1":
        <td><image src="../static/complete.svg"></td>
        %else:
        <td><image src="../static/incomplete.svg"></td>
        %end

        <td>
            <a href="/delete{{str(row['_id'])}}">
                <image src="../static/delete.svg">
            </a>
        </td>
    </tr>
    %end
    </form>
    </table>