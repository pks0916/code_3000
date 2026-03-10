import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    rows = []

    for i in range(len(anon_df)):
        a_age = anon_df.loc[i, "age"]
        a_zip = anon_df.loc[i, "zip3"]
        a_gender = anon_df.loc[i, "gender"]

        count = 0
        match_name = ""

        for j in range(len(aux_df)):
            b_age = aux_df.loc[j, "age"]
            b_zip = aux_df.loc[j, "zip3"]
            b_gender = aux_df.loc[j, "gender"]

            if a_age == b_age and a_zip == b_zip and a_gender == b_gender:
                count = count + 1
                match_name = aux_df.loc[j, "name"]

        if count == 1:
            rows.append([anon_df.loc[i, "anon_id"], match_name])

    out = pd.DataFrame(rows, columns=["anon_id", "matched_name"])
    return out
    


def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    
    rate = len(matches_df) / len(anon_df)
    return rate
