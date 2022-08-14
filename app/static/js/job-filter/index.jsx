const JobFilter = ()=>{
    React.useEffect(() => {
        extractUrl()
    }, []);
    const [state, setState] = React.useState({
        id : '',
        status: '',
        link: '',
        date_from: '',
        date_to: ''
    });
    const [path, setPath] = React.useState({
        currentPage: window.location.href,
        previousPage: '',
        nextPage: ''
    });
    const extractUrl = () => {
        const local_state = {...state};
        const loc = window.location.href;
        const queries = loc.split('?');
        if (queries.length === 2) {
            const sub_queries = queries[1].split('&');
            sub_queries.forEach((item) => {
                let ssb = item.split('=');
                try{
                    local_state[ssb[0]] = ssb[1]
                } catch (e) {
                    console.log(e)
                }
            });
            setState({...state, ...local_state})
        }
    };
    const handleChange = ({target: { name, value}}) => {
        const new_state = {...state};
        new_state[name] = value;
        setState({...new_state});
        handlePathChange()
        // console.log(name, value);
    };
    const handlePathChange = () => {
        const _path = window.location.href;
        const path_split = _path.split('?');
        let base = path_split[0];
        let page = '';
        let currentPage = 1;
        if (path_split.length === 2) {
            page = path_split[1].split('&')[0]
            currentPage = page.split('=')[1]
        }
        let output = ``;
        for (let key in state){
            if(state.hasOwnProperty(key) && !!state[key]) {
                output += `${key}=${state[key]}&`
            }
        }
        const nextPath = {
            currentPage: `${base}?page=${currentPage}&${output}`,
            previousPage: `${base}?page=${+currentPage - 1 >= 1 ? +currentPage - 1 : 1}&${output}`,
            nextPage: `${base}?page=${+currentPage+1}&${output}`,
        };
        setPath({...path,
          ...nextPath
        });
        return nextPath;
    };
    const onSubmit = (e) => {
        const nxt = handlePathChange();
        setPath({...path, ...nxt});
        window.location.href = nxt.currentPage
    };
    return (
        <div>
            <div className="d-flex justify-content-between">
                <div>
                    <label>Status</label>
                    <br/>
                    <select name="status" value={state.status} onChange={handleChange} id="status">
                        <option />
                        <option value="QUEUED">QUEUED</option>
                        <option value="PENDING">PENDING</option>
                        <option value="RUNNING">RUNNING</option>
                        <option value="RAN">RAN</option>
                        <option value="TIMEOUT">TIMEOUT</option>
                        <option value="KEYWORD_CANNIBALIZATION">KEYWORD_CANNIBALIZATION</option>
                        <option value="FAILED">FAILED</option>
                    </select>
                </div>
                <div>
                    <label>#JobID</label>
                    <br/>
                    <input type="text" name="id" value={state.id} size={8} onChange={handleChange}/>
                </div>
                
                <div>
                    <label>Date From</label>
                    <br/>
                    <input type="date" name="date_from" value={state.date_from} onChange={handleChange}/>
                </div>
                <div>
                    <label>Date To</label>
                    <br/>
                    <input type="date" name="date_to" value={state.date_to} onChange={handleChange}/>
                </div>
                <div className="align-self-end">
                    <button onClick={onSubmit} className="btn btn-sm btn-primary">Search</button>
                </div>
            </div>
            <br/>
            <div className="d-flex justify-content-between">
                <a onClick={onSubmit} className="btn btn-sm btn-primary" href={path.previousPage}>Previous</a>
                <a onClick={onSubmit} className="btn btn-sm btn-primary" href={path.nextPage}>Next</a>
            </div>
        </div>
    )
};

ReactDOM.render(<JobFilter />, document.getElementById('job-filter'));
