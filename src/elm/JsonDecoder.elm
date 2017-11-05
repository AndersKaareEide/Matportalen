module JsonDecoder exposing (..)

import Json.Decode exposing (..)
import Json.Decode.Pipeline exposing (..)
import Types exposing (..)


visitDecoder : Decoder Visit
visitDecoder =
    decode Visit
        |> required "dato" string
        |> required "orgnummer" string
        |> required "total_karakter" string
        |> required "navn" string


getRestaurantsProper : Value -> List Restaurant
getRestaurantsProper value =
    let
        visits =
            decodeVisits value
    in
        getRestaurants (getUniqueOrgnrs visits) visits


getRestaurants : List Visit -> List Visit -> List Restaurant
getRestaurants uniqueList visitList =
    List.map (\visit -> { name = visit.name, orgnr = visit.orgnr, visits = List.filter (\e -> e.orgnr == visit.orgnr) visitList }) visitList


getUniqueOrgnrs : List Visit -> List Visit
getUniqueOrgnrs list =
    case list of
        [] ->
            []

        x :: xs ->
            let
                temp =
                    getUniqueOrgnrs xs
            in
                if not (checkIfExists temp x.orgnr) then
                    (x :: temp)
                else
                    temp


checkIfExists : List Visit -> String -> Bool
checkIfExists visits orgnr =
    List.any (\visit -> visit.orgnr == orgnr) visits


decodeVisits : Value -> List Visit
decodeVisits json =
    Result.withDefault [] (decodeValue (field "entries" (list visitDecoder)) json)


testDecoder : Value -> Result String (List Visit)
testDecoder json =
    decodeValue (field "entries" (list visitDecoder)) json



--asda
