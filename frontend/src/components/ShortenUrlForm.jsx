/* eslint no-unused-vars: 1 */

import React, { useCallback, useState } from 'react';
import axios from "axios";

const ShortenUrlForm = () => {
    const [value, setValue] = useState('');
    const [status, setStatus] = useState('');

    const onChange = useCallback(
        (e) => {
            setValue(e.target.value)
        }
    );

    function copyTextToClipboard(text) {
        navigator.clipboard.writeText(text);
    }

    const onSubmit = useCallback(
        (e) => {
            e.preventDefault();
            axios.post('http://127.0.0.1:8000/shorturl/', {"url" : value})
            .then((response) => {
                console.log(response);
                setStatus({ type: 'success', 'short_url': response.data.short_url});
                copyTextToClipboard(response.data.short_url)
            }, (error) => {
                console.log(error);
                setStatus({ type: 'error', 'error': error.response.data.url[0]});
            });
        }
    );


    return (
        <form onSubmit={onSubmit}>
            <label htmlFor="shorten">
                Url:
                <input
                    placeholder="Url to shorten"
                    id="shorten"
                    type="text"
                    value={value}
                    onChange={onChange}
                />
            </label>
            <input type="submit" value="Shorten and copy URL" />
            {status.type === "error" && (
                <div className="error">{status.error}</div>
            )}
            {status.type === "success" && (
                <div>shortened url - {status.short_url} - copied!  </div>
            )}
        </form>
    );
};

export default ShortenUrlForm;
