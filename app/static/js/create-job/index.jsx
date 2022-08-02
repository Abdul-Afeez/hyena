const CreateJob = ()=>{
    React.useEffect(() => {
    }, []);
    const [state, setState] = React.useState({
        status : '',
        url: '',
        link: ''
    });

    const handleChange = ({target: { name, value}}) => {
        const new_state = {...state};
        new_state[name] = value;
        setState({...new_state});
    };

    const onSubmit = (e) => {

    };
    return (
        <form method="POST">
            <div className="col-md-4 col-sm-6">
                <div className="mt-2">
                    <label>Status</label>
                    <br/>
                    <select className="form-control" name="status" value={state.status} onChange={handleChange} id="status">
                        <option value="QUEUED">QUEUED</option>
                        <option value="PENDING">PENDING</option>
                        <option value="RUNNING">RUNNING</option>
                        <option value="RAN">RAN</option>
                        <option value="TIMEOUT">TIMEOUT</option>
                        <option value="FAILED">FAILED</option>
                    </select>
                </div>
                <div className="mt-2">
                    <label>Url</label>
                    <br/>
                    <input className="form-control" type="text" name="url" value={state.url} size={8} onChange={handleChange}/>
                </div>
                <div className="mt-2">
                    <label>Link</label>
                    <br/>
                    <input className="form-control"  type="text" name="link" value={state.link} size={20} onChange={handleChange}/>
                </div>
                <br/>
                <div className="align-self-end">
                    <button onClick={onSubmit} className="btn btn-primary">Create</button>
                </div>
            </div>
            <br/>
        </form>
    )
};

ReactDOM.render(<CreateJob />, document.getElementById('create-job'));
