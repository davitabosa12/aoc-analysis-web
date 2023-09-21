import { useEffect } from "react";
import AoCApiService from "../api/aoc-api-service/AoCApiService";
export default function FormSearch(props) {
    useEffect(() => {
        const api = new AoCApiService("http://localhost:5000");
        api.getAllAoCReports().then((listOfAocs) => {
            console.table(listOfAocs);
        });
    });
    return (
        <>
        <form>
            <label htmlFor="">Project</label>
            <select>
                <option>Project 1</option>
                <option>Project 2</option>
                <option>Project 3</option>
            </select>
            <label htmlFor="">Atom</label>
            <select name="" id="">
                <option>Atom 1</option>
                <option>Atom 2</option>
                <option>Atom 3</option>
            </select>
            <input type="submit" value="Search" onClick={(e) => {
                e.preventDefault();
            }} />
        </form>
        </>
    )
}