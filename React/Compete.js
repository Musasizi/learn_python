import React from 'react';

export default function HomePage() {
    const [user, setUser] = React.useState(null);

    async function fetchUser(e) {
        e.preventDefault();
        
        const headers = {
            method: 'GET',
        };

        const givenName = e.target.value;
        try {
            const apiData = await fetch(`api.github.com/${givenName}`, headers);
            setUser(apiData);
        } catch (error) {
            console.error('error');
        }
    }

    if (user === null) {
        return <div>Loading...</div>;
    }


    return (
        <div>
            <h1>GITHUB PROFILE FINDER </h1>
            <input type='text' placeholder='Username' />
            <input type='submit' onClick={fetchUser} />

            {user && (
                <div>
                    <p>Username:</p>
                    <p>{user?.username}</p>
                    <p>Repositories:</p>
                    <p>{user?.number_of_repositories}</p>

                </div>
            )}

        </div>
    );
}
