from pandas import DataFrame, read_csv

from scripts.config import DATA_IMPORT_LOCATION, IMPORT_FILE_NAME, logger


def import_data() -> DataFrame:
    """Import data.

    Returns:
        Imported data.
    """
    logger.debug(
        f'Importing data from: {DATA_IMPORT_LOCATION}',
    )
    with open(
        f'{DATA_IMPORT_LOCATION}/{IMPORT_FILE_NAME}.csv',
        'r',
        encoding='utf-8-sig',
    ) as csv_file:
        data = read_csv(
            csv_file,
            delimiter=',',
        )
        logger.debug(
            f'Import completed, {len(data.index)} rows imported',
        )
        return data


def clear_data(
    data: DataFrame,
    save_filename: str = 'cleared_data',
) -> DataFrame:
    """Delete rows with empty values.

    Args:
        data: provided dataframe.
        save_filename: filename to save data.

    Returns:
        Cleared dataframe.
    """
    cleared_data = data.dropna()
    with open(
        f'{DATA_IMPORT_LOCATION}/{save_filename}.csv',
        'w',
        encoding='utf-8-sig',
    ) as cleared_file:
        cleared_data.to_csv(cleared_file, lineterminator='\n')
    logger.debug(
        f'Empty values deleted, {len(data.index)} rows left',
    )
    return cleared_data


def filter_data(
    data: DataFrame,
    save_filename: str = 'filtered_data',
) -> DataFrame:
    """Leave only even ids and released movies.

    Args:
        data: provided dataframe.
        save_filename: filename to save data.

    Returns:
        Filtered dataframe.
    """
    filtered_data = data[(data.id % 2 == 0) & (data.status == 'Released')]
    with open(
        f'{DATA_IMPORT_LOCATION}/{save_filename}.csv',
        'w',
        encoding='utf-8-sig',
    ) as filtered_file:
        filtered_data.to_csv(filtered_file, lineterminator='\n')
    logger.debug(
        f'DataFrame filtered, {len(data.index)} rows left',
    )
    return filtered_data


def aggregate_income(
    data: DataFrame,
    save_filename: str = 'income_data',
) -> DataFrame:
    """Aggregate incomes of genres.

    Args:
        data: provided dataframe.
        save_filename: filename to save data.

    Returns:
        Filtered dataframe.
    """
    income_data = data.groupby('genre_names').agg({'revenue': 'sum'})
    with open(
        f'{DATA_IMPORT_LOCATION}/{save_filename}.csv',
        'w',
        encoding='utf-8-sig',
    ) as income_file:
        income_data.to_csv(income_file, lineterminator='\n')
    logger.debug(
        f'Income summed up, {len(income_data.index)} rows left',
    )
    return income_data


def calculate_rate_votes_to_budget(
    data: DataFrame,
    save_filename: str = 'rate_data',
) -> DataFrame:
    """Calculate rate of average vote to budget.

    Args:
        data: provided dataframe.
        save_filename: filename to save data.

    Returns:
        Filtered dataframe.
    """
    rate_data = (
        data.groupby('genre_names').agg({'vote_average': 'mean'})[
            'vote_average'
        ]
        / data.groupby('genre_names').agg({'budget': 'mean'})['budget']
    ).rename('vote_to_budget_ratio', axis=0)
    with open(
        f'{DATA_IMPORT_LOCATION}/{save_filename}.csv',
        'w',
        encoding='utf-8-sig',
    ) as rate_file:
        rate_data.to_csv(rate_file, lineterminator='\n')
    logger.debug(
        f'Rate calculcated, {len(rate_data.index)} rows left',
    )
    return rate_data


def main() -> None:
    """Start main code."""
    data = import_data()
    cleared_data = clear_data(data)
    filtered_data = filter_data(cleared_data)
    aggregate_income(filtered_data)
    calculate_rate_votes_to_budget(filtered_data)


if __name__ == '__main__':
    main()
