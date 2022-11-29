from mrjob.job import MRJob
from mrjob.job import MRStep
class RatingsBreakdown(MRJob):
    
    def steps(self):
        return [
            
            MRStep(mapper=self.mapper_get_ratings,
            reducer=self.reducer_count_ratings)
    ]

    def mapper_get_ratings(self, _, line):
        ( Index, Moviename,Genre ) = line.split('::')
        yield Genre, 1

    def reducer_count_ratings(self, key, values):
        yield key, sum(values)
if __name__ == '__main__':
    RatingsBreakdown.run()
