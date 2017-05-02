import socket
import struct


def get_questions(query):
    question = query[0:12]
    qtype = query[12:14]
    qclass = query[14:16]
    return (question, qtype, qclass)

def get_answers(responses):
    name = responses[0:2]
    atype = responses[2:4]
    aclass = responses[4:6]
    ttl = responses[6:10]
    datalen = responses[10:12]
    addr = responses[12:16]
    return (name, atype, aclass, ttl, datalen, addr)

def parse_query(query):
    trans_id = query[0][0:2].encode('hex')
    flags = query[0][2:4].encode('hex')
    num_of_ques = int(query[0][4:6].encode('hex'))
    num_of_ans = int(query[0][6:8].encode('hex'))
    num_of_authrrs = int(query[0][8:10].encode('hex'))
    num_of_addrrs = int(query[0][10:12].encode('hex'))
    index = 12
    queries = [query[0][index+i:index+i+16].encode('hex') for i in  range(num_of_ques)]
    all_questions = map(get_questions, queries)
    index = index + num_of_ques*16
    responses = [query[0][index+i:index+i+16].encode('hex') for i in range(num_of_ans)]
    all_answers = map(get_answers, responses)
    index = index + num_of_ans*16
    add_records = query[index:]
    print queries


def main():
    port = 53

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.bind(('', port))

    while True:
        query =  s.recvfrom(1024)
        parse_query(query)

if __name__== '__main__':
    main()
