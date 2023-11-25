-module(mylib).
-export([start/0, store/2, retrieve/1, init_store/1]).

start() ->
    Pid = spawn(fun() -> init_store([]) end),
    register(key_value_store, Pid),
    Pid.

init_store(Data) ->
    receive
        {store, Key, Value, From} ->
            NewData = lists:keyreplace(Key, 1, Data, {Key, Value}),
            From ! {ok, Key, Value},
            init_store(NewData);
        {retrieve, Key, From} ->
            case lists:keyfind(Key, 1, Data) of
                {Key, Value} ->
                    From ! {ok, Key, Value};
                false ->
                    From ! {error, not_found}
            end,
            init_store(Data);
        stop ->
            ok
    end.

store(Key, Value) ->
    key_value_store ! {store, Key, Value, self()},
    receive
        Result ->
            io:format("Store Result: ~p~n", [Result]),
            Result
    end,
    timer:sleep(1000).

retrieve(Key) ->
    key_value_store ! {retrieve, Key, self()},
    receive
        Result ->
            io:format("Retrieve Result: ~p~n", [Result]),
            Result
    after 100 % 100 milliseconds timeout
        -> timeout
    end.

    
% Example usage:
% c(mylib).

% mylib:start().

% mylib:store("name", "Alice").

% mylib:retrieve("name").
